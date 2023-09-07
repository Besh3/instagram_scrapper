# instagram_scrapper
Data analysis for CoW Mentions on instagram platform

## Metrics
#### metric[0] must be one of the following values: 
impressions, reach, follower_count, email_contacts, phone_call_clicks, text_message_clicks, get_directions_clicks, website_clicks, profile_views, audience_gender_age, audience_locale, audience_country, audience_city, online_followers, accounts_engaged, total_interactions, likes, comments, shares, saves, replies, engaged_audience_demographics, reached_audience_demographics, follower_demographics, follows_and_unfollows, profile_links_taps&since=2023-06-01&until=2023-08-01

## Step 1 Starting a local web service
## Seting up webhooks for instagram @mentions and mentioned comments
set one up for this demo using Python SimpleHTTPServer.

1. Create a new directory, we'll call it ~/ngrok-rocks
2. Move into that directory and create a file named index.html with a single line of text: Hello, World!
3. From that folder, run python3 -m http.server. This will start a web server on port 8000 serving the contents of that directory.
4. Open http://localhost:8000 in your browser

### Step 2: Install the ngrok Agent
choco install ngrok
You can test everything is working by running ngrok -h 

### Step 3: Connect your agent to your ngrok account
ngrok config add-authtoken TOKEN. Sign in ngrok Dashboard and get your Authtoken.

## Step 4: Start ngrok
Start ngrok by running the following command.

ngrok http 8000