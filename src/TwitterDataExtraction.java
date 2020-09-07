import java.io.BufferedWriter;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.HashMap;

import twitter4j.Twitter;

public class TwitterDataExtraction {
	private static String AccessToken = "";
	private static String AccessSecret = "";
	private static String ConsumerKey = "";
	private static String ConsumerSecret = "";
	private static HashMap authTokenMap = new HashMap();

	public static void main(String[] args) {
		authTokenMap.put("AccessToken", AccessToken);
		authTokenMap.put("AccessSecret", AccessSecret);
		authTokenMap.put("ConsumerKey", ConsumerKey);
		authTokenMap.put("ConsumerSecret", ConsumerSecret);

		TwitterAuthentication auth = new TwitterAuthentication();
		TwitterSearchData twitterData = new TwitterSearchData();
		Twitter authObject = null;

	 	String keyWords = "DalhousieUniversity OR Canada OR University OR Halifax OR CanadaEducation";
		ArrayList tweets = new ArrayList();
		authObject = auth.authenticateUser(authTokenMap);
		tweets = twitterData.getTwitterData(authObject, keyWords);

		try {
			BufferedWriter wr = new BufferedWriter(new FileWriter("tweets.txt"));
			for (int i = 0; i < tweets.size(); i++) {
				wr.write(tweets.get(i).toString());
				wr.newLine();
			}
			wr.close();
		} catch (Exception e) {
			System.out.println("Error Occured");
		}
	}
}
