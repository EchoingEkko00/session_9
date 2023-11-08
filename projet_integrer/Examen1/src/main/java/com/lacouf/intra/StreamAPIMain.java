package com.lacouf.intra;

import java.util.stream.Collectors;
import java.util.stream.Stream;

public class StreamAPIMain {
    public static void main(String[] args) {
        final String question = Stream.of(
                        new Student("Mathieu", "Tremblay", 30, Genre.HOMME),
                        new Student("Nathalie", "Smith", 25, Genre.FEMME),
                        new Student("Isabelle", "Giroux", 18, Genre.FEMME),
                        new Student("Jean", "Gauthier", 35, Genre.HOMME)
                ).filter(s -> s.genre == Genre.FEMME)
                .map(s -> s.firstName + " " + s.lastName)
                .collect(Collectors.joining(", "));
        System.out.println(question);

    }
    enum Genre {
        HOMME,
        FEMME,
        NONGENRE
    }
    record Student(String firstName, String lastName, int age, Genre genre){}
}
