package com.example.dummy;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.text.DecimalFormat;
import java.util.Arrays;
import java.util.List;

import lombok.AllArgsConstructor;

@AllArgsConstructor
public class MatcherResponse {

    @JsonProperty("source_element")
    private String sourceElement;

    @JsonProperty("target_element")
    private String targetElement;

    @JsonProperty("score")
    private String score;

    public static List<MatcherResponse> getDummyResponse() {
        return Arrays.asList();
    }
}
