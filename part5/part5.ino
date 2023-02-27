#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Int32.h>
#include <std_msgs/Bool.h>

ros::NodeHandle nh;

std_msgs::String str_msg;
std_msgs::Int32 int_msg;

void boolCallback(const std_msgs::Bool& msg)
{
  digitalWrite(13, msg.data);
}
ros::Publisher str_chatter("str_chatter", &str_msg);
ros::Publisher num_chatter("num_chatter", &int_msg);


ros::Subscriber<std_msgs::Bool> bool_listener("bool_listener", &boolCallback );

int value = 0;
char str_1[10] = "Un zpacio";


void setup() {
  // put your setup code here, to run once:
  pinMode(13,OUTPUT);
  nh.initNode();
  nh.advertise(str_chatter);
  nh.advertise(num_chatter);
  nh.subscribe(bool_listener);

}

void loop() {
  // put your main code here, to run repeatedly:
  str_msg.data = str_1;
  str_chatter.publish( &str_msg );

  int_msg.data = value;
  num_chatter.publish( &int_msg );

  value++;
  nh.spinOnce();
  delay(500);
  
}
