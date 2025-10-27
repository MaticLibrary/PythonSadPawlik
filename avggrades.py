

def calculate_avg(grades_list):
    num = 0
    total = 0
    if (len(grades_list) == 0):
        return 0
    else:
        for i in range(len(grades_list)):
            total += grades_list[i]             # just loop and sum
            
        avg = total/len(grades_list)
        return  avg 
    

def calculate_avgInteligent(grades_list):
    return sum(grades_list) / len(grades_list) if grades_list else 0


def main():
    grades =  [4,3,5,2,5,6,4,2,4,6,2,5,3,5,6,4,2,5,3,4,6]      # grades 

    avg = calculate_avg(grades)
    print ("Casual avg is: " , avg)

    avgInteligent = calculate_avgInteligent(grades)
    print ("Inteligent avg is: " , avg)
    

if __name__ == '__main__':
    main()
