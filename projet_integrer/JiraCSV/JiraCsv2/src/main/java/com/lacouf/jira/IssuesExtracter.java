package com.lacouf.jira;

import com.lacouf.JiraConfig;
import lombok.AllArgsConstructor;
import org.apache.commons.lang3.StringUtils;
import org.json.JSONArray;
import org.json.JSONObject;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Base64;

@AllArgsConstructor
public class IssuesExtracter {
    private final HttpClient client;
    private final HttpRequest request;

    public IssuesExtracter(String projectIn, String sprintIn) {
        System.out.println("Authorization: " + getHeader());
        client = HttpClient.newBuilder()
                           .version(HttpClient.Version.HTTP_1_1)
                           .build();

        var project = StringUtils.isNotBlank(projectIn) ? projectIn : JiraConfig.PROJECT;
        var sprint = StringUtils.isNotBlank(sprintIn) ? sprintIn : JiraConfig.SPRINT_NAME;
        var params = ("?jql=project = \"" + project +
             "\" AND Sprint = \"" + sprint + "\"" +
             "&maxResults=" + JiraConfig.MAX_RESULTS + "&fields=" + JiraConfig.FIELDS)
            .replace(" ", "%20")
            .replace("\"", "%22");
        System.out.println("\nparams: " + params);

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

    public JSONArray getAllIssues() {
        String body = "";
        try {
            body = client.send(request, HttpResponse.BodyHandlers.ofString())
                         .body();
            var results = new JSONObject(body);
            return results.getJSONArray("issues");
        } catch (IOException | InterruptedException e) {
            throw new RuntimeException(e);
        } catch (Exception e) {
            System.err.println("---- Erreur de parsing de la réponse ----");
            System.err.println(e.getLocalizedMessage());
            System.err.println("Réponse de JIRA: ");
            System.err.println(body);
            System.exit(1);
        }
        return null;
    }
}
