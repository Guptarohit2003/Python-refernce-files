#include <bits/stdc++.h>
using namespace std;
void Merge(int *A, int s, int mid, int e)
{
    int *B = new int[10000];
    int i = s,j = mid+1,k = s;
    while (i<=mid && j<=e)
    {
        if (A[i]<A[j])
        {
            B[k++] = A[i++];
        }
        else
        {
            B[k++] = A[j++];
        }
    }
    while (i<=mid)
    {
        B[k++] = A[i++];
    }
    while (j<=e)
    {
        B[k++] = A[j++];
    }
    for (int i = 0; i < e+1; i++)
    {
        A[i] = B[i];
    }
    delete[] B;
}
void MergeSort(int *A, int s, int e)
{
    if (s >= e)
    {
        return;
    }
    int mid = (s + e) / 2;
    MergeSort(A, s, mid);
    MergeSort(A, mid + 1, e);
    Merge(A, s, mid, e);
}
int main()
{
    int n;
    cin >> n;
    int A[n];
    for (int i = 0; i < n; i++)
    {
        cin >> A[i];
    }
    MergeSort(A, 0, n - 1);
    for (int i = 0; i < n; i++)
    {
        cout << A[i] << " ";
    }
    cout << endl;
    return 0;
}