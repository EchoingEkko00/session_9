package com.lacouf.iterator;

import java.util.*;

public class IteratorEverydayDemo {

	public static void main(String[] args) {
		Collection<String> col;  // Voir Javadoc
		List<String> names = new ArrayList<>();
		//Set<String> names = new HashSet<>();

		names.add("Bryan");
		names.add("Aaron");
		names.add("Jason");

		System.out.println("Names size: " + names.size());
		
		Iterator<String> namesItr = names.iterator();
		
		//for(int i = 0; i < names.size(); i++) {
		//	String name = names.get(i);
		//}
		
		//for (String name : names) {
		//	System.out.println(name);
		//}
		
		while(namesItr.hasNext()) {
			String name = namesItr.next();
			System.out.println(name);
			namesItr.remove();
		}
		
		System.out.println("Names size: " + names.size());
	}
}
