class reusable:
    def dropColumns(self,df,columns):
        # if you want to drop multiple columns then we have to use *
        df=df.drop(*columns)
        return df
    def dropDuplicates(self,df,columns):
        df=df.dropDuplicates(columns)
        return df
    
    
    