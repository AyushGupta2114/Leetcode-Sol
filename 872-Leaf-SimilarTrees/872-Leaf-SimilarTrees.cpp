        vector<int>tree1;
        vector<int>tree2;

        dfs(root1,tree1);
        dfs(root2,tree2);
    if(tree1==tree2)
    {
    return true;
    }
    else
    {
        return false;
    }
    }
};
[3,5,1,6,2,9,8,null,null,7,4]
