package com.lacouf.observer.observer2;

import java.time.LocalDateTime;
import java.util.Timer;
import java.util.TimerTask;

public class TimeSubject extends Subject{
    private LocalDateTime time = LocalDateTime.now();
    private Timer timer;

    public LocalDateTime getTime() {
        return time;
    }

    public TimeSubject() {
        new Timer().schedule(new TimerTask() {
            @Override
            public void run() {
                time = LocalDateTime.now();
                notifyObservers();
            }
        }, 1000, 1000);
    }
}
