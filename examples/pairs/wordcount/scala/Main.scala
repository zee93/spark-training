import org.apache.spark._

object Main {
  def main(args: Array[String]) {
    val conf = new SparkConf().setAppName("test").setMaster("local[*]")
    val sc = new SparkContext(conf)
    val words_count_rdd = sc.textFile("..\\input").flatMap(_.split).map(_ -> 1).reduceByKey(a,b => a + b)

  }
}
