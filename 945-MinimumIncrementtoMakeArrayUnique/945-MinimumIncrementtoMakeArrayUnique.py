            prev=nums[i]
                nums[i]=prev+1
            if (nums[i]<=prev):
                count+=(prev+1)-nums[i]
        for i in range(len(nums)):
        nums.sort()
        count=0
        prev=-1
        #     prev = nums[i];

        #         nums[i] = prev + 1;
        #     }

        return count
        # count=0
        # # nums.sort()
        # print(nums)
        # print("")
        # for i in range(0,len(nums)-1):
[
