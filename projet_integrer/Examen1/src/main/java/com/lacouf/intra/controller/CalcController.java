package com.lacouf.intra.controller;

import com.lacouf.intra.model.Result;
import com.lacouf.intra.service.Calcservice.CalcService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@CrossOrigin(origins = "http://localhost:3000")
public class CalcController {

    private CalcService calcService;

    public CalcController(CalcService calcService) {
        this.calcService = calcService;
    }


    @GetMapping("/add/{one}/{two}")
    public ResponseEntity<Result> add(@PathVariable Integer one, @PathVariable Integer two) {
        return ResponseEntity.ok(new Result(one,two,calcService.add(one, two)));
    }

    @GetMapping("/sub/{one}/{two}")
    public ResponseEntity<Result> sub(@PathVariable Integer one, @PathVariable Integer two) {
        return ResponseEntity.ok(new Result(one,two,calcService.sub(one, two)));
    }
}
