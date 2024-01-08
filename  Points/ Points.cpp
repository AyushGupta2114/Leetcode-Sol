        {
            return 1;
        }
        cout<<root->val;
        if(root->val>=low && root->val<=high)
        {
            s=s+root->val;
        }
        rangeSumBST(root->left,low,high);

        rangeSumBST(root->right,low,high);
        return s;
    }
    
};
[10,5,15,3,7,null,18]
