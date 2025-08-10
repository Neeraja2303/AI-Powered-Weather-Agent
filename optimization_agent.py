def give_tips(crop):
    tips = {
        'rice': 'Use puddled soil and maintain standing water for better yields.',
        'wheat': 'Sow in cool, dry season. Use nitrogen-rich fertilizer.',
        'maize': 'Grow in warm areas with well-drained soil. Fertilize at sowing and 30 days later.'
    }
    return tips.get(crop.lower(), "Follow local agri-extension recommendations.")
