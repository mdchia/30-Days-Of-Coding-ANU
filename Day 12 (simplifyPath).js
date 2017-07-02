function simplifyPath(path) {
    dirs=path.split('/');
    final_dirs=[,]
    for(i in dirs){
       curr_dir=dirs[i]
        if(curr_dir==''||curr_dir=='.'){
           continue
           }
        else if(curr_dir=='..'){
           final_dirs.pop()
           }
        else{
           final_dirs.push(curr_dir)
        }
    }
    // from https://stackoverflow.com/a/2132045
    final_dirs=final_dirs.filter(function(x) { return x !== null; })

    final_dirs=final_dirs.join('/')
    final_dirs='/'+final_dirs
    return final_dirs;
}
