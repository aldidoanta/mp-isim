package com.example.dummy;

import com.fasterxml.jackson.annotation.JsonProperty;

public class MatcherRequest {

    @JsonProperty("source_schema")
    private String sourceSchema;

    @JsonProperty("target_schema")
    private String targetSchema;
}
