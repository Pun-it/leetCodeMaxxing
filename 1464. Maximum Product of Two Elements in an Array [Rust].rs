impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut biggest = 0 ;
        let mut second_biggest = 0;
        for i in 0..nums.len() {
            if nums[i] > biggest {
                second_biggest = biggest;
                biggest = nums[i];
            }
            else { 
                if second_biggest > nums[i]{
                    second_biggest = second_biggest;
                } 
                else{
                    second_biggest = nums[i];
                }
            }
        }
        return (biggest-1)*(second_biggest-1);
    }
}