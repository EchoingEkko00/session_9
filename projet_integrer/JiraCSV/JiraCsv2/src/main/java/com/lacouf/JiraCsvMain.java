package com.lacouf;

/**
 * Fonctionne avec JiraCloud Connector.  S'assurer d'avoir un API key valide et généré de l'adresse suivante:
 * https://id.atlassian.com/manage-profile/security/api-tokens
 */
public class JiraCsvMain {

    public static void main(String[] args) throws Exception {
        if (args.length < 3) {
            System.out.println("Usage:");
            System.out.println("  From REST API:");
            System.out.println("    java -jar JiraCSV.jar EQ2 \"Sprint 1\" 21-09-2022");
            System.out.println("       where EQ2 is project, Sprint 1 is the actual sprint");
            System.out.println("       and 21-09-2022 is the date to start seeing work logs");
            //System.out.println("  With CSV file:");
            //System.out.println("    java -jar JiraCSV.jar file.csv 21-10-2020 15:00");
            System.exit(0);
        }

        if (args.length == 0) {
            new JiraCloudConnector()
                .getAllIssuesAsync()
                .thenAccept(entries -> new JiraReporter().printRestReport(entries, JiraConfig.START_DATE_TIME))
                .join();
        } else {
            var project = args[0];
            var sprint = args[1];
            var dateFrom = args[2];

            new JiraCloudConnector(project, sprint)
                .getAllIssuesAsync()
                .thenAccept(entries -> new JiraReporter().printRestReport(entries, dateFrom + " 00:00"))
                .join();
//            JiraCsvParser parser = new JiraCsvParser();
//            List<LogWorkEntry> logWorkEntries = parser.parse(args[0]);
//            new JiraReporter().printCsvReport(logWorkEntries, args[1]);
        }
    }
}
