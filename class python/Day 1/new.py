def social_super_algorithm(user_data):
    # FB: Relationships & Community
    community_score = analyze_fb_connections(user_data.friends, user_data.groups)
    
    # Insta: Visual Interests & Trends
    interest_score = analyze_insta_interactions(user_data.likes, user_data.reels_watched)
    
    # Combined Logic: Personalized Recommendation
    # W1 and W2 are weights given to different behaviors
    final_feed_priority = (W1 * community_score) + (W2 * interest_score)
    
    return generate_custom_feed(final_feed_priority)