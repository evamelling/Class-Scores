##
# class_scores.py
# Calculates the mean, lowest and highest scores
# of class_a list and class_b list combined
# Then prints them out
# Author: Eva Melling
# Date: 02.03.2023

def combined_list_average():
    # Create variables - count and total_score
    count = 0
    total_score = 0

    # Loop through combined_list with a for loop
    for score in combined_list:
        count += 1  # add 1 for everytime it loops through
        total_score += score    # add score onto total_score

    # Store total_score divided by score in variable called mean
    mean = total_score / count

    return mean
    

if __name__ == "__main__":

    # Defines class_a list and class_b list
    class_a = [44, 33, 28, 47, 12, 28, 32, 31, 11, 39, 40, 26, 36]
    class_b = [19, 26, 38, 31, 30, 42, 44, 14, 27, 43, 46, 49, 24, 26, 36]

    # Combined list equals class_a list plus class_b list
    combined_list = class_a + class_b
    
    # Print the title - 'Class Scores Part 1'
    print("Class Scores Part 1\n")

    # Print mean, lowest and highest score
    print("The mean score is: {}".format(combined_list_average()))
    print("The lowest score is: {}".format(min(combined_list)))
    print("The highest score is: {}".format(max(combined_list)))


