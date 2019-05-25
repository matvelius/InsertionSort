import UIKit

let array = [3, 5, -4, 8, 11, 1, -1, 6]

//  let array = [4, 6, 1]

let targetSum = 10



func twoNumberSum(array: [Int], targetSum: Int) -> Array<Int> {
    
    
    for number in array {
        
        let difference = targetSum - number
        
        for secondNumber in array where secondNumber != number {
            
            if secondNumber == difference {
                
                if number < secondNumber {
                    
                    return [number, secondNumber]
                    
                } else {
                    
                    return [secondNumber, number]
                    
                }
                
            }
            
        }
        
    }
    
    return []
    
}



print(twoNumberSum(array: array, targetSum: targetSum))
