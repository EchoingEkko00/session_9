package com.lacouf.jira;

import com.lacouf.JiraCloudConnector;
import com.lacouf.JiraConfig;
import com.lacouf.JiraReporter;
import org.json.JSONArray;

/**
 * Fonctionne avec JiraCloud Connector.  S'assurer d'avoir un API key valide et généré de l'adresse suivante:
 * https://id.atlassian.com/manage-profile/security/api-tokens
 */
public class JiraExtractorMain {

    public static void main(String[] args) throws Exception {
        if (args.length < 2) {
            System.out.println("Usage:");
            System.out.println("  From REST API:");
            System.out.println("    java -jar JiraExtractorMain.jar EQ2 \"Sprint 1\" ");
            System.out.println("       where EQ2 is project, Sprint 1 is the actual sprint");
            System.exit(0);
        }

        var project = args[0];
        var sprint = args[1];

        final JSONArray allIssues = new IssuesExtracter(project, sprint)
            .getAllIssues();

        System.out.println(allIssues.toString());

        //.thenAccept(entries -> new JiraReporter().printRestReport(entries, dateFrom + " 00:00"))
            //.join();
//            JiraCsvParser parser = new JiraCsvParser();
//            List<LogWorkEntry> logWorkEntries = parser.parse(args[0]);
//            new JiraReporter().printCsvReport(logWorkEntries, args[1]);

    }
}
