package com.example.dummy;

import java.util.List;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;

@RestController
public class MatcherController {

	@Operation(description = "Given a source schema and a target schema, returns a schema mapping along with the similarity score.")
	@ApiResponses(value = { 
		@ApiResponse(responseCode = "200", content = { @Content(mediaType = "application/json",
			schema = @Schema(implementation = MatcherResponse.class)) }),
	})
	@PostMapping("matcher/match-schemas")
	public ResponseEntity<List<MatcherResponse>> matchSchemas(@RequestBody MatcherRequest request) {
		return ResponseEntity.ok(MatcherResponse.getDummyResponse());
	}
}
