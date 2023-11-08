package com.lacouf.intra.service.Calcservice;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit.jupiter.SpringExtension;

@ContextConfiguration(classes = {CalcService.class})
@ExtendWith(SpringExtension.class)
class CalcServiceTest {
    @Autowired
    private CalcService calcService;

    @Test
    void testAdd() {
        assertEquals(4, calcService.add(2, 2));
        assertEquals(5, calcService.add(3, 2));
        assertEquals(3, calcService.add(1, 2));
        assertEquals(2, calcService.add(0, 2));
    }

    @Test
    void testSub() {
        assertEquals(0, calcService.sub(3, 3));
        assertEquals(-2, calcService.sub(1, 3));
        assertEquals(-3, calcService.sub(0, 3));
        assertEquals(-4, calcService.sub(-1, 3));
    }
}

