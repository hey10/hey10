import java.io.*;
public class ForLoopSyntax{
	public static boolean checkFollowingCharacter(String str,char ch1,char ch2){
		return (str.charAt(str.indexOf(ch1)+1)==ch2)?true:false;
	}

	public static boolean checkCharacters(String str,char ch1,char ch2){
		int count=0;
		for(int i=str.indexOf(ch1)+1;i<str.indexOf(ch1);i++)
			if(str.charAt(i)=='(' || str.charAt(i)==')' || str.charAt(i)=='{' || str.charAt(i)=='}')
				count++;

		return (count==0)?true:false;
	}
	
	public static boolean checkSemicolon(String str){
		int count=0;
		char[] ch=str.toCharArray();
		for(char c:ch)
			if(c==';')
				count++;

		return (count==2)?true:false;
	}
	

	public static boolean checkForLoopSyntax(String str){
		boolean status=false;
		if(checkFollowingCharacter(str,'r','(')==true){
			if(checkSemicolon(str)==true && checkCharacters(str,'(',')')==true){
				if(checkFollowingCharacter(str,')','{')==true){
					if(checkCharacters(str,'{','}')==true){
						status=true;
					}
					else
						status=false;
				}
				else
					status=false;
			}
			else
				status=false;
		}	
		else
			status=false;

		return status;
	}

	public static void main(String[] args)throws Exception{
		System.out.println("Enter the For Loop Statement=");
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		String str=br.readLine();
		if(checkForLoopSyntax(str)==true)
			System.out.println("Valid For Loop Syntax");
		else
			System.out.println("Invalid For Loop Syntax");
	}
}