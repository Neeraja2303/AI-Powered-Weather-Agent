def soil_advice(ph, nitrogen):
    if ph < 5.0:
        if nitrogen < 20:
            return "Highly acidic and nitrogen-deficient soil. Add lime and nitrogen-rich fertilizers. Ideal for rice or blueberries."
        else:
            return "Highly acidic soil. Add lime. Suitable for rice, sweet potato, or blueberries."

    elif 5.0 <= ph < 5.5:
        if nitrogen < 40:
            return "Acidic and nitrogen-deficient. Apply lime and organic compost. Grow rice, millets, or sweet potato."
        else:
            return "Moderately acidic. Apply lime. Suitable for soybeans or oats."

    elif 5.5 <= ph < 6.5:
        if nitrogen < 50:
            return "Slightly acidic and low in nitrogen. Add compost or urea. Suitable for corn, barley, and pulses."
        else:
            return "Good soil. Suitable for wheat, maize, groundnuts, and vegetables."

    elif 6.5 <= ph < 7.5:
        if nitrogen < 60:
            return "Neutral pH with moderate nitrogen deficiency. Use urea or ammonium nitrate. Suitable for most crops like wheat and pulses."
        else:
            return "Ideal soil conditions. Grow any crops including vegetables, cereals, and legumes."

    elif 7.5 <= ph < 8.5:
        if nitrogen < 60:
            return "Alkaline soil with moderate nitrogen. Add gypsum and nitrogen fertilizer. Good for cotton, barley, and beetroot."
        else:
            return "Alkaline but fertile soil. Grow sorghum, barley, or sugar beet."

    else:
        return "Highly alkaline soil. Apply gypsum and organic matter. Grow salt-tolerant crops like barley or mustard."
