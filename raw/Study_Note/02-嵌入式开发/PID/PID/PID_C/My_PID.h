#ifndef _MY_PID_H_
#define _MY_PID_H_

#include "stdint.h"

struct MY_PID_Type
{
  volatile double SetPoint;/*目标值*/
  volatile double OutPut;/*输出值*/
					 double PID_P;
					 double PID_I;
					 double PID_D;
  volatile double Error;/*当前次误差*/	
  volatile double Error_Last;/*上一次误差*/
	volatile double Error_Prev;/*上两次误差*/
	volatile double Sun_Error;/*累计误差*/
};


#endif

