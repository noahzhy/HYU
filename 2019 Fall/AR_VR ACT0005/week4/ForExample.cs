using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ForExample : MonoBehaviour
{
    public GameObject cube;
    // Start is called before the first frame update
    void Start()
    {
        for(int i = 0; i < 10; i++)
        {
            for(int k = 0; k < 10; k++)
            {
                Instantiate(cube, new Vector3(i * 2, 0, k * 2), Quaternion.identity);
            }
            
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
