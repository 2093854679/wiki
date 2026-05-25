/******************** (C) COPYRIGHT 2023 ***********************************************************
 * @NAME: MY_PID.c
 * @author:
 * @copyright:
 * @versions:V1.0.0
 * @fun:PID算法
 * 
 * @updata: V1.0.0  2023-05-25  create a file
**************************************************************************************************/
#include "MY_PID.h"
#include <stdlib.h>


/*************************************************************************************************
 * @name:MY_PID_Init
 * @fun: PID结构体初始化
 * @input:MY_PID_Type 结构体  P:比例  I：积分  D 微分
 * @retv: 正常：0  异常：负数
 * @annot: 
**************************************************************************************************/
int MY_PID_Init(struct MY_PID_Type *pid,double P,double I,double D)
{
  if(pid == NULL)
		goto _State;
  if(P == 0)
		goto _State;
	pid->PID_P = P;
	pid->PID_I = I;
	pid->PID_D = D;	
	pid->OutPut = 0;
	pid->Error = 0;
	pid->Error_Last = 0;
	pid->Error_Prev = 0;
	pid->Sun_Error  = 0;
	return 0;
	
_State:
	return -1;
}


/*************************************************************************************************
 * @name:MY_PID_Increment
 * @fun: 增量式PID计算  
 * @input:MY_PID_Type 结构体  Value：当前值   Out_Max：输出限幅最大值  Out_Min：输出限幅最小值
 * @retv: 输出值
 * @annot: 
**************************************************************************************************/
double MY_PID_Increment(struct MY_PID_Type *pid,double Value,double Out_Max,double Out_Min)
{
  pid->Error = pid->SetPoint - Value;/*计算当前次误差*/
  pid->OutPut +=  (pid->PID_P * (pid->Error - pid->Error_Last)) + /*比例环*/
	                (pid->PID_I * pid->Error) + /*积分环*/
	                (pid->PID_D * (pid->Error - 2*pid->Error_Last + pid->Error_Prev));/*微分环*/
	pid->Error_Prev = pid->Error_Last; /*误差存储*/
	pid->Error_Last = pid->Error;
  if(pid->OutPut > Out_Max)
		pid->OutPut = Out_Max;
	else if(pid->OutPut < Out_Min)
		pid->OutPut = Out_Min;
	return pid->OutPut;
}

/*************************************************************************************************
 * @name:MY_PID_Location
 * @fun: 位置式PID计算  
 * @input:MY_PID_Type 结构体  Value：当前值   Out_Max：输出限幅最大值  Out_Min：输出限幅最小值
 * @retv: 输出值
 * @annot: 
**************************************************************************************************/
double MY_PID_Location(struct MY_PID_Type *pid,double Value,double Out_Max,double Out_Min)
{
  pid->Error = pid->SetPoint - Value;/*计算当前次误差*/
	pid->Sun_Error += pid->Error;/*计算累计误差*/
	
  pid->OutPut =   (pid->PID_P * pid->Error) + /*比例环*/
	                (pid->PID_I * pid->Sun_Error) + /*积分环*/
	                (pid->PID_D * (pid->Error - pid->Error_Last));/*微分环*/
	pid->Error_Prev = pid->Error_Last; /*误差存储*/
	pid->Error_Last = pid->Error;
  if(pid->OutPut > Out_Max)
		pid->OutPut = Out_Max;
	else if(pid->OutPut < Out_Min)
		pid->OutPut = Out_Min;
	return pid->OutPut;
}


/*****************************************end**************************************************************/
