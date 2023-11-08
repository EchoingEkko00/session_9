package com.lacouf.intra.controller;

import static org.mockito.Mockito.when;

import com.lacouf.intra.service.Calcservice.CalcService;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mockito;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit.jupiter.SpringExtension;
import org.springframework.test.web.servlet.request.MockHttpServletRequestBuilder;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;

@ContextConfiguration(classes = {CalcController.class})
@ExtendWith(SpringExtension.class)
class CalcControllerTest {
    @Autowired
    private CalcController calcController;

    @MockBean
    private CalcService calcService;

    @Test
    void testAdd() throws Exception {
        when(calcService.add(Mockito.<Integer>any(), Mockito.<Integer>any())).thenReturn(2);
        MockHttpServletRequestBuilder requestBuilder = MockMvcRequestBuilders.get("/add/{one}/{two}", 1, 1);
        MockMvcBuilders.standaloneSetup(calcController)
                .build()
                .perform(requestBuilder)
                .andExpect(MockMvcResultMatchers.status().isOk())
                .andExpect(MockMvcResultMatchers.content().contentType("application/json"))
                .andExpect(MockMvcResultMatchers.content().string("{\"one\":1,\"two\":1,\"result\":2}"));
    }

    @Test
    void testSub() throws Exception {
        when(calcService.sub(Mockito.<Integer>any(), Mockito.<Integer>any())).thenReturn(1);
        MockHttpServletRequestBuilder requestBuilder = MockMvcRequestBuilders.get("/sub/{one}/{two}", 1, 1);
        MockMvcBuilders.standaloneSetup(calcController)
                .build()
                .perform(requestBuilder)
                .andExpect(MockMvcResultMatchers.status().isOk())
                .andExpect(MockMvcResultMatchers.content().contentType("application/json"))
                .andExpect(MockMvcResultMatchers.content().string("{\"one\":1,\"two\":1,\"result\":1}"));
    }
}

