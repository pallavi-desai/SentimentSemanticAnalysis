import java.util.ArrayList;
import java.util.List;

import twitter4j.Query;
import twitter4j.QueryResult;
import twitter4j.Status;
import twitter4j.Twitter;

public class TwitterSearchData {
	public static ArrayList getTwitterData(Twitter authObject, String topic) {
		ArrayList tweetList = new ArrayList();
		try {
			Query query = new Query(topic);
			QueryResult result = null;
			System.out.println(query.toString());
			do {
				result = authObject.search(query);
				List <Status>tweets = result.getTweets();
				for (Status tweet : tweets) {
					tweetList.add(tweet.getText());
				}
			} while (result.hasNext() == true);
		} catch (Exception e) {
			e.printStackTrace();
			System.out.println("Failed to search tweets: " + e.getMessage());
		}
		return tweetList;
	}
}
