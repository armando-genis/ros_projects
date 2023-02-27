/*
 * rosserial Publisher Example
 * Prints "hello world!"
 */

// Use the following line if you have a Leonardo or MKR1000
//#define USE_USBCON

#include <ros.h>
#include <std_msgs/UInt16.h>

ros::NodeHandle nh;

std_msgs::UInt16 uint8_t_msg;
ros::Publisher potentiometer("potentiometer", &uint8_t_msg);

int sensorValue;

void setup()
{

  nh.initNode();
  nh.advertise(potentiometer);
  
}

void loop()
{
  sensorValue = analogRead(A0);
  uint8_t_msg.data = sensorValue;
  potentiometer.publish( &uint8_t_msg );
  nh.spinOnce();
  delay(1000);/simplescreenrecorder.mp4

}