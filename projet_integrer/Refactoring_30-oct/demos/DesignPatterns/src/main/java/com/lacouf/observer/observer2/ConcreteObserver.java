package com.lacouf.observer.observer2;

public class ConcreteObserver implements Observer{

    private final ConcreteSubject subject;

    public ConcreteObserver(ConcreteSubject subject) {
        this.subject = subject;
    }


    @Override
    public void update() {
        System.out.println(subject.getLocalDateTime());
    }
}
