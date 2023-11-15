package com.lacouf;

public class JiraConfig {

    public static final String USER_EMAIL = "lacouf@gmail.com";
    public static final String API_TOKEN_A21 = "3cgjZy1q2Hm2QxxvjHKA60CF"; //https://id.atlassian.com/manage-profile/security pour générer
    public static final String API_TOKEN = "ATATT3xFfGF0bq21EV8byjKTCt_wgCDsVmRgf9_1f4V4r-spsr2KBI2iu2aP1JhYOOBgkD7XMYw8rqeA5C-Aml2yKVvUFrKp_Sm-rbjcAgJo4tODYJiAEgT2mVfQ3W6Z3LdOC7XkELmAR2kBgZK1e_42qXT30jrRLfJv3L3cXSgFYyHVMgGwSPI=DB4AF355";
    public static final String SITE_URL = "https://420-565-a23.atlassian.net";
    public static final String PROJECT = "EQ3";  // "EQ2", "OS"
    public static final String SPRINT_NAME = ""; //si null, recherche par date seulement
    public static final String START_DATE_TIME = "21-09-2023 00:00"; // dd-MM-yyyy
    public static final boolean INCLUDE_EMPTY_COMMENT = true;

    //Do not change
    public static final String FIELDS = "id,worklog,parent,summary";
    public static final int MAX_RESULTS = 100;
}
