package com.example.dummy;

import java.util.List;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MatcherController {

	@PostMapping("matcher/match-schemas")
	public ResponseEntity<List<MatcherResponse>> greeting(@RequestBody MatcherRequest request) {
		return ResponseEntity.ok(MatcherResponse.getDummyResponse());
	}
}
