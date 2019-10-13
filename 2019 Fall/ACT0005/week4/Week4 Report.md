# VR/AR 캡스톤 디자인 4주차 과제

**2018000337  
장호우  
컴퓨터소프트웨어학부**  


1. switch문을 사용하여 인스펙터 창에서 시험점수(0~100점)를 입력하면, 점수를 학점으로(A-100~90,B-89~80,C-79~70,D-69~60,F-59~)변환하는 프로그램 만들기

   ```c#
    public class firstScriptf : MonoBehaviour {
        public int score = 85;
        public char grade = 'F';
        void Start() {
            switch (score / 10) {
                case 10:
                    grade = 'A';
                    break;
                case 9:
                    grade = 'A';
                    break;
                case 8:
                    grade = 'B';
                    break;
                case 7:
                    grade = 'C';
                    break;
                case 6:
                    grade = 'D';
                    break;
                default:
                    grade = 'F';
                    break;
            }
            Debug.Log("Grade is " + grade);
        }
   ```

   

   <img src="E:\HYU\2019 Fall\ACT0005\Snipaste_2019-10-01_15-39-49.png" style="zoom:60%;" />

   

2. for문을 사용하여 오브젝트 생성 및 배치하기

   ```c#
   public class firstScriptf : MonoBehaviour {
       public GameObject cube;
       void Start() {
           for (int i = 0; i < 9; i++) {
               for (int j = i; j < 9; j++) {
                   Instantiate(cube, new Vector3(i*2, 0, j*2), Quaternion.identity);
               }
           }
       }
   ```



<img src="E:\HYU\2019 Fall\ACT0005\Snipaste_2019-10-01_15-31-20.png" style="zoom:60%;" />




3. 배열 공부하기 & 배열과 for문을 사용하여 숫자 10개를 입력 받아 모두 더하는 프로그램 만들기

```c#
public int[] sum_nums = new int[10] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
public int total_sum = 0;
void Start() {
    for (int i = 0; i<sum_nums.Length; i++) {
        total_sum += sum_nums[i];
    }
    Debug.Log("Sum is " + total_sum);
}
```



<img src="E:\HYU\2019 Fall\ACT0005\Snipaste_2019-10-01_16-01-13.png" style="zoom:60%;" />

