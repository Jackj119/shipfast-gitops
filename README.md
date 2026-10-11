# shipfast-gitops

# Main Issue:
My initial deployment file was pointing at an image that had a name that didn't match on Docker Hub; after correcting the name and pushing the change through Git, Argo CD was redeployed and the pods began to run properly.
