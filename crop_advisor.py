def recommend_crop(temp, rainfall, soil_type):
    if temp > 25 and rainfall > 150:
        return "rice"
    
    elif (temp<10 and temp==18):
        return "sorghum"
    elif temp == 25 and rainfall < 100:
        return "wheat"
    elif soil_type == 'sandy':
        return "groundnut"
    else:
        return "maize"