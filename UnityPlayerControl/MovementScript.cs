using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MovementScript : MonoBehaviour
{
    Rigidbody rigidBody; //Represents the character's RigidBody component
    float speed = 0.05f, fallRounding = 0.01f;//Speed is the walk speed modifier; fall rounding is used for semi-accurate fall detection
    bool isFalling = false; //This bool stores if the character is falling or on the ground
    int jumpHeight = 200; //This value modifies how high the character jumps

    private void Start()
    {
        rigidBody = gameObject.GetComponent<Rigidbody>(); //We assign the rigidBody variable
    }

    private void FixedUpdate()
    { //The following lines handle the horizontal movement
        if (Input.GetKey(KeyCode.W))
        {
            gameObject.transform.Translate(Vector3.forward * speed);
        }
        if (Input.GetKey(KeyCode.S))
        {
            gameObject.transform.Translate(-Vector3.forward * speed);
        }
        if (Input.GetKey(KeyCode.A))
        {
            gameObject.transform.Translate(-Vector3.right * speed);
        }
        if (Input.GetKey(KeyCode.D))
        {
            gameObject.transform.Translate(Vector3.right * speed);
        }
        if (!isFalling) //If we aren't falling and we've pressed space, jump
        {
            if (Input.GetKeyDown(KeyCode.Space))
            {
                rigidBody.velocity = Vector3.zero;
                rigidBody.AddForce(Vector3.up * jumpHeight);
            }
        }

        if (Mathf.Abs(rigidBody.velocity.y) > fallRounding) //If the absolute value of the y velocity is less than the rounding variable, we aren't falling
            isFalling = true;
        else
            isFalling = false;
        
    }
}
