import java.util.HashMap;

import twitter4j.Twitter;
import twitter4j.TwitterFactory;
import twitter4j.conf.ConfigurationBuilder;

public class TwitterAuthentication {
	public static Twitter authenticateUser(HashMap<String, String> authTokenMap) {

		ConfigurationBuilder cb = new ConfigurationBuilder();
		cb.setDebugEnabled(true);
		cb.setJSONStoreEnabled(true);
		cb.setOAuthConsumerKey(authTokenMap.get("ConsumerKey"));
		cb.setOAuthConsumerSecret(authTokenMap.get("ConsumerSecret"));
		cb.setOAuthAccessToken(authTokenMap.get("AccessToken"));
		cb.setOAuthAccessTokenSecret(authTokenMap.get("AccessSecret"));
		cb.setHttpConnectionTimeout(100000);

		Twitter twitter = new TwitterFactory(cb.build()).getInstance();
		return twitter;

	}
}
