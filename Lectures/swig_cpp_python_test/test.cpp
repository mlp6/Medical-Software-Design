#include "calc.h"
#include <gtest/gtest.h>

calc calc;

TEST(calc_add_two, success)
{
    EXPECT_EQ(calc.add_two(3, 2), 5);
    EXPECT_NE(calc.add_two(3, 2), 8);
}


int main(int argc, char **argv){
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
