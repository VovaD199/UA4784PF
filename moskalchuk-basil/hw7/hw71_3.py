def count_characters(text):
    """Calculates the number of characters in text"""
    result = {}
    
    for char in text:
        if char in result:
            result[char] +=1
        else:
            result[char] = 1

    return result       
  
    
    
    