package com.lacouf.observer.observer2;

public class ClientObserverDemo {
    public static void main(String[] args) {
        ConcreteSubject subject = new ConcreteSubject();
        Observer observer = new ConcreteObserver(subject);
        subject.attachObserver(observer);
    }
}
