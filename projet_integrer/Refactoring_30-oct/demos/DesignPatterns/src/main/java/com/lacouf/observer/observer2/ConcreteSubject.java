package com.lacouf.observer.observer2;

import java.time.LocalDateTime;
import java.util.Timer;
import java.util.TimerTask;

public class ConcreteSubject extends Subject{

    private LocalDateTime localDateTime;
    private TimeSubject timeSubject = new TimeSubject();
    private Timer timer = new Timer();

    public ConcreteSubject() {
        timer.schedule(new TimerTask() {
            @Override
            public void run() {
                localDateTime = LocalDateTime.now();
                notifyObservers();
            }
        }, 1000, 1000);
    }
    public LocalDateTime getLocalDateTime() {
        return localDateTime;
    }

}
