package com.lacouf.intra.service.Calcservice;

import org.springframework.stereotype.Service;

@Service
public class CalcService {
    public int add(Integer one, Integer two) {
        return one + two;
    }

    public int sub(Integer one, Integer two) {
        return one - two;
    }
}
