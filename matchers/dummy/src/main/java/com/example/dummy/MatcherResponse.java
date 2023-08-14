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
        DecimalFormat decimalFormat = new DecimalFormat("#.###");
        return Arrays.asList(
            new MatcherResponse("dummy_source_element_1", "dummy_target_element_1", decimalFormat.format(0.5)),
            new MatcherResponse("dummy_source_element_2", "dummy_target_element_2", decimalFormat.format(0.2556))
        );
    }
}
