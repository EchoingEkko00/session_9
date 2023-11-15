package com.lacouf;

import org.apache.commons.lang3.StringUtils;
import org.json.JSONArray;
import org.json.JSONObject;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.LocalDateTime;
import java.util.Base64;
import java.util.LinkedList;
import java.util.List;
import java.util.concurrent.CompletableFuture;

public class JiraCloudConnector {

    private final HttpClient client;
    private final HttpRequest request;

    public JiraCloudConnector() {
        this(JiraConfig.PROJECT, JiraConfig.SPRINT_NAME);
    }

    public JiraCloudConnector(String projectIn, String sprintIn) {
        System.out.println("Authorization: " + getHeader());
        client = HttpClient.newBuilder()
                .version(HttpClient.Version.HTTP_1_1)
                .build();

        var project = StringUtils.isNotBlank(projectIn) ? projectIn : JiraConfig.PROJECT;
        var sprint = StringUtils.isNotBlank(sprintIn) ? sprintIn : JiraConfig.SPRINT_NAME;
        var params = ("?jql=project = \"" + project +
                (StringUtils.isNotBlank(sprint) ? "\" AND Sprint = \"" + sprint : "") +
                "\" AND timespent != 0" + "&maxResults=" + JiraConfig.MAX_RESULTS + "&fields=" + JiraConfig.FIELDS)
                .replace(" ", "%20")
                .replace("\"", "%22");
        System.out.println(params);

        request = HttpRequest.newBuilder()
                .GET()
                .uri(URI.create(JiraConfig.SITE_URL + "/rest/api/3/search" + params))
                .header("Authorization", getHeader())
                .build();

        System.out.println("Headers: " + request.headers().toString());
        System.out.println("Request URI:" + request.uri());

    }

    private String getHeader() {
       return "Basic "
            + Base64.getEncoder().encodeToString((JiraConfig.USER_EMAIL + ":" + JiraConfig.API_TOKEN).getBytes());
    }

    public CompletableFuture<List<LogWorkEntry>> getAllIssuesAsync() {
        return client.sendAsync(request, HttpResponse.BodyHandlers.ofString())
                .thenApply(this::parseJsonResults)
                .thenApply(this::parseToEntity);
    }

    private JSONArray parseJsonResults(HttpResponse<String> rb) {
        //System.out.println(rb.body());
        try {
            //System.out.println(rb.body());
            var results = new JSONObject(rb.body());
            return results.getJSONArray("issues");
        }
        catch (Exception e) {
            System.err.println("---- Erreur de parsing de la réponse ----");
            System.err.println(e.getLocalizedMessage());
            System.err.println("Réponse de JIRA: ");
            System.err.println(rb.body());
            System.exit(1);
        }
        return null;
    }

    private List<LogWorkEntry> parseToEntity(JSONArray array) {
        var list = new LinkedList<LogWorkEntry>();

        array.forEach(o -> {
            var obj = (JSONObject) o;
            obj.getJSONObject("fields").getJSONObject("worklog").getJSONArray("worklogs").forEach(wl -> {
                var log = (JSONObject) wl;
                try {
                    list.add(LogWorkEntry.builder()
                            .taskId(obj.getString("key"))
                            .userTask(getSummary(obj))
                            .userName(log.getJSONObject("author").getString("displayName"))
                            .logWorkDescription(getComment(log))
                            .logWorkDate(log.getString("created"))
                            .logWorkSeconds(log.getInt("timeSpentSeconds"))
                            .logWorkDateTime(LocalDateTime.parse(
                                log.getString("created")
                                   .replaceFirst("\\.[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]", "")))
                            .build());
                }
                catch (Exception e) {
                    System.err.println("Caught \"" + e.getMessage() + "\" on a worklog from "
                        + obj.getString("key") + " by "
                        + log.getJSONObject("author").getString("displayName"));
                }
            });
        });

        return list;
    }

    private String getComment(JSONObject log) {
        String value;
        try {
            value = log.getJSONObject("comment").getJSONArray("content")
                       .getJSONObject(0).getJSONArray("content")
                       .getJSONObject(0).getString("text");
        }
        catch (Exception e) {
            if (JiraConfig.INCLUDE_EMPTY_COMMENT)
                value = "--- EMPTY COMMENT ---";
            else
                throw e;
        }
        return value;
    }

    private String getSummary(JSONObject obj) {
        StringBuilder sb = new StringBuilder();
        if (obj.getJSONObject("fields").has("parent"))
            sb.append(obj.getJSONObject("fields").getJSONObject("parent").getJSONObject("fields").getString("summary")).append(" ");

        sb.append(obj.getJSONObject("fields").getString("summary"));
        return sb.toString();
    }
}
