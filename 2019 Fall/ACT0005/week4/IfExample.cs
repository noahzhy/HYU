using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class IfExample : MonoBehaviour
{
    public int number = 0;
    // Start is called before the first frame update
    void Start()
    {
        if (number <= 100 && number >= 90)
        {
            Debug.Log("A");
        }else if (number >= 80)
        {
            Debug.Log("B");
        }
        else if (number >= 70)
        {
            Debug.Log("C");
        }
        else if (number >= 60)
        {
            Debug.Log("D");
        }
        else 
        {
            Debug.Log("F");
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
