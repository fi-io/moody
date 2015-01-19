package edu.iiit.sample;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Locale;
import java.util.ResourceBundle;

public class PropertiesDemo {
	final public static Locale[] supportedLocales = { Locale.GERMAN, Locale.ENGLISH };
	ResourceBundle labels = null;
	public PropertiesDemo(Locale localeVal) {
		labels = ResourceBundle.getBundle("LabelsBundle", localeVal);
	}
	
	private void showText() {
		StringBuilder sb = new StringBuilder();
		sb.append("Hello! My ").append(labels.getString("s1")).append(" consists of ")
		.append("a ").append(labels.getString("s2")).append(", a ").append(labels.getString("s3"))
		.append(" and a ").append(labels.getString("s4")).append(".");
		System.out.println(sb.toString());
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		System.out.println("Enter 0 for German and 1 for English:");
		InputStreamReader in = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(in);
		int input = Integer.parseInt(br.readLine());
		PropertiesDemo props = new PropertiesDemo(supportedLocales[input]);
		props.showText();
	}
}
