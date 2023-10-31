package com.lacouf.observer.observer2;

import java.util.ArrayList;
import java.util.List;

public abstract class Subject {
    private List<Observer> observers = new ArrayList<>();

    public void attachObserver(Observer observer) {
        observers.add(observer);
    }

    public void notifyObservers() {
        observers.stream().forEach(o -> o.update());
    }
}
