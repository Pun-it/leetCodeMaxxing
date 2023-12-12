class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxProduct($nums) {
        $biggest = 0;
        $sbiggest = 0;
        for ($x = 0; $x <= count($nums) ; $x+=1) {
            if ($nums[$x] > $biggest){
                $sbiggest = $biggest;
                $biggest = $nums[$x];
            }
            else{
                $sbiggest = max($sbiggest,$nums[$x]);
            }
        }
        return ($biggest -1)*($sbiggest -1);
    }
}