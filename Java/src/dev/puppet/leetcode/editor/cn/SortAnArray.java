package dev.puppet.leetcode.editor.cn;

/**
 * 题目：912 排序数组
 * @author puppet
 * @since 2022-05-31 16:28:20
 */
public class SortAnArray {
    public static void main(String[] args) {
        Solution solution = new SortAnArray().new Solution();
    }
    
    //leetcode submit region begin(Prohibit modification and deletion)
    class Solution {
        /**
         * @Tag 排序算法、快排
         * @Solution
         * @TimeComplexity O(NlogN)
         * @SpaceComplexity O(n)
         */
        public int[] sortArray(int[] nums) {
            if (nums.length <= 1) return nums;
            int start = 0;
            int end = nums.length - 1;
            process(nums, start, end);
            return nums;
        }
        
        private void process(int[] nums, int start, int end) {
            if (start >= end) return;
            
            int pivot = nums[start];
            int left = start, right = end;
            while (left < right) {
                while (left < right) {
                    if (nums[right] < pivot) {
                        nums[left] = nums[right];
                        break;
                    }
                    right--;
                }
                while (left < right) {
                    if (nums[left] > pivot) {
                        nums[right] = nums[left];
                        break;
                    }
                    left++;
                }
            }
            // 注意需要将位置填回去
            nums[left] = pivot;
            process(nums, start, left - 1);
            process(nums, left + 1, end);
        }
    }
//leetcode submit region end(Prohibit modification and deletion)

}